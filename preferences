import mari

_set_name = 'tdPrefs'
_default_maximize = False
_current_maximize = _default_maximize


#-------------------------------------------------------------------------------
# Preference functions
#-------------------------------------------------------------------------------
def registerPreferences():
    global _current_maximize
    global _default_maximize
    mari.prefs.set("tdTools/Preferences/maximize", _current_maximize)
    mari.prefs.setDefault("tdTools/Preferences/maximize", _default_maximize)
    mari.prefs.setDisplayName("tdTools/Preferences/maximize", 'Maximize At Start')
    mari.prefs.setChangedScript("tdTools/Preferences/maximize", 'td.lib.libPrefs.maximizePreferenceChanged()')


# ------------------------------------------------------------------------------
def loadPreferences():
    settings = mari.Settings()
    global _set_name
    settings.beginGroup(_set_name)

    try:
        global _current_maximize
        global _default_maximize
        _current_maximize = False if int(settings.value('maximize', _default_maximize)) == 0 else True

    except ValueError, e:
        mar.utils.message("Error loading preferences '%s':<p>%s" % (_set_name, str(e)), "Mari - Error loading preferences", icon=3)

    settings.endGroup()


# ------------------------------------------------------------------------------
def savePreferences():
    settings = mari.Settings()
    global _set_name
    settings.beginGroup(_set_name)

    global _current_maximize
    settings.setValue('maximize', 1 if _current_maximize else 0)

    settings.endGroup()


#-------------------------------------------------------------------------------
def updateAndSavePreferences():
    global _current_maximize
    mari.prefs.set('tdTools/Preferences/maximize', _current_maximize)

    savePreferences()



# ------------------------------------------------------------------------------
def maximizePreferenceChanged():
    global _current_maximize
    _current_maximize = mari.prefs.get('tdTools/Preferences/maximize')
    savePreferences()

if _current_maximize:
    mari.app.maximize()

if mari.app.isRunning():
    loadPreferences()
    registerPreferences()
    savePreferences()
