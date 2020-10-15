import { DARK_MODE_TOGGLE, ToggleDarkModeAction } from "./Actions";

export interface SystemState {
  darkMode: boolean;
}

const initialState = {
  darkMode: false,
};

function systemReducer(
  state = initialState,
  action: ToggleDarkModeAction
): SystemState {
  switch (action.type) {
    case DARK_MODE_TOGGLE:
      return { ...state, darkMode: !state.darkMode };
    default:
      return state;
  }
}

export { systemReducer };
