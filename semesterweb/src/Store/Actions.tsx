const DARK_MODE_TOGGLE = "DARK_MODE_TOGGLE";

interface ToggleDarkModeAction {
  type: typeof DARK_MODE_TOGGLE;
}

function toggleDarkMode(): ToggleDarkModeAction {
  return { type: DARK_MODE_TOGGLE };
}

export { DARK_MODE_TOGGLE, toggleDarkMode, ToggleDarkModeAction };
