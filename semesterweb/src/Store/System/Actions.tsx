const DARK_MODE_TOGGLE = "DARK_MODE_TOGGLE";
const OPEN_SIDEBAR = "OPEN_SIDEBAR";
const LOADING_TOGGLE = "LOADING_TOGGLE";

interface ToggleDarkModeAction {
  type: typeof DARK_MODE_TOGGLE;
}

interface OpenSideBarAction {
  type: typeof OPEN_SIDEBAR;
}

interface LoadingToggleAction {
  type: typeof LOADING_TOGGLE;
}

function toggleDarkMode(): ToggleDarkModeAction {
  return { type: DARK_MODE_TOGGLE };
}

function openSideBar(): OpenSideBarAction {
  return { type: OPEN_SIDEBAR };
}

function toggleLoading(): LoadingToggleAction {
  return { type: LOADING_TOGGLE };
}

export { DARK_MODE_TOGGLE, toggleDarkMode, ToggleDarkModeAction };
export { OPEN_SIDEBAR, openSideBar, OpenSideBarAction };
export { LOADING_TOGGLE, LoadingToggleAction, toggleLoading };
