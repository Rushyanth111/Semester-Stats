import {
  DARK_MODE_TOGGLE,
  ToggleDarkModeAction,
  OPEN_SIDEBAR,
  OpenSideBarAction,
} from "./Actions";

export interface SystemState {
  darkMode: boolean;
  sideBarOpen: boolean;
}

const initialState = {
  darkMode: false,
  sideBarOpen: false,
};

function systemReducer(
  state = initialState,
  action: ToggleDarkModeAction | OpenSideBarAction
): SystemState {
  switch (action.type) {
    case DARK_MODE_TOGGLE:
      return { ...state, darkMode: !state.darkMode };
    case OPEN_SIDEBAR:
      return { ...state, sideBarOpen: !state.sideBarOpen };

    default:
      return state;
  }
}

export { systemReducer };
