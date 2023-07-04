#!/usr/bin/env python3.7

import asyncio
import iterm2
import logging

logger = logging.getLogger('macos_theme_sync')
dark_profile = None
light_profile = None


async def get_profiles(connection):
    global dark_profile
    global light_profile
    partialProfiles = await iterm2.PartialProfile.async_query(connection)
    for partial in partialProfiles:
        if partial.name == "Default":
            dark_profile = await partial.async_get_full_profile()
        elif partial.name == "Light":
            light_profile = await partial.async_get_full_profile()


async def session_set_profile(app, profile):
    for window in app.windows:
        for tab in window.tabs:
            for session in tab.sessions:
                await session.async_set_profile(profile)


async def on_theme_change(connection):
    app = await iterm2.async_get_app(connection)
    window = app.current_window
    initial_theme = await app.async_get_theme()
    initial_parts = initial_theme[0].split(" ")

    try:
        if "dark" in initial_parts:
            await session_set_profile(app, dark_profile)
            logger.info('Initial theme is dark')
        else:
            await session_set_profile(app, light_profile)
            logger.info('Initial theme is light')
    except Exception as e:
        print(traceback.format_exc())
        print(e)

    async with iterm2.VariableMonitor(connection, iterm2.VariableScopes.APP, "effectiveTheme", None) as mon:
        while True:
            # Block until theme changes
            theme = await mon.async_get()
            # Themes have space-delimited attributes, one of which will be light or dark.
            parts = theme.split(" ")
            try:
                if "dark" in parts:
                    await session_set_profile(app, dark_profile)
                    logger.info('Initial theme is dark')
                else:
                    await session_set_profile(app, light_profile)
                    logger.info('Initial theme is light')
            except Exception as e:
                print(traceback.format_exc())
                print(e)


async def on_session_create(connection):
    app = await iterm2.async_get_app(connection)
    window = app.current_window

    async with iterm2.NewSessionMonitor(connection) as mon:
        while True:
            session_id = await mon.async_get()
            session = app.get_session_by_id(session_id)
            theme = await app.async_get_theme()
            parts = theme[0].split(" ")
            try:
                if "dark" in parts:
                    await session.async_set_profile(dark_profile)
                    logger.info('Initial theme is dark')
                else:
                    await session.async_set_profile(light_profile)
                    logger.info('Initial theme is light')
            except Exception as e:
                print(traceback.format_exc())
                print(e)


async def main(connection):
    await get_profiles(connection)
    asyncio.create_task(on_theme_change(connection))
    asyncio.create_task(on_session_create(connection))

iterm2.run_forever(main)
