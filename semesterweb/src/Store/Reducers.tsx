import { DARK_MODE_TOGGLE, ToggleDarkModeAction } from "./Actions";

export interface GlobalState {
  darkMode: boolean;
}

const initialState = {
  darkMode: false,
};

function SemesterApp(
  state = initialState,
  action: ToggleDarkModeAction
): GlobalState {
  switch (action.type) {
    case DARK_MODE_TOGGLE:
      return { ...state, darkMode: !state.darkMode };
    default:
      return state;
  }
}

export default SemesterApp;
