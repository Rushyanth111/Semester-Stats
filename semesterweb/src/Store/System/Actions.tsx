const DARK_MODE_TOGGLE = "DARK_MODE_TOGGLE";
const OPEN_SIDEBAR = "OPEN_SIDEBAR";

interface ToggleDarkModeAction {
  type: typeof DARK_MODE_TOGGLE;
}

interface OpenSideBarAction {
  type: typeof OPEN_SIDEBAR;
}

function toggleDarkMode(): ToggleDarkModeAction {
  return { type: DARK_MODE_TOGGLE };
}

function openSideBar(): OpenSideBarAction {
  return { type: OPEN_SIDEBAR };
}

export { DARK_MODE_TOGGLE, toggleDarkMode, ToggleDarkModeAction };
export { OPEN_SIDEBAR, openSideBar, OpenSideBarAction };
