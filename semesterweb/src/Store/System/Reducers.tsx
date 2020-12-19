import {
  DARK_MODE_TOGGLE,
  ToggleDarkModeAction,
  OPEN_SIDEBAR,
  OpenSideBarAction,
  LOADING_TOGGLE,
  LoadingToggleAction,
} from "./Actions";

export interface SystemState {
  darkMode: boolean;
  sideBarOpen: boolean;
  loadingToggle: boolean;
}

const initialState = {
  darkMode: false,
  sideBarOpen: false,
  loadingToggle: false,
};

function systemReducer(
  state = initialState,
  action: ToggleDarkModeAction | OpenSideBarAction | LoadingToggleAction
): SystemState {
  switch (action.type) {
    case DARK_MODE_TOGGLE:
      return { ...state, darkMode: !state.darkMode };
    case OPEN_SIDEBAR:
      return { ...state, sideBarOpen: !state.sideBarOpen };
    case LOADING_TOGGLE:
      return { ...state, loadingToggle: !state.loadingToggle };
    default:
      return state;
  }
}

export { systemReducer };
