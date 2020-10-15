import { combineReducers } from "redux";
import { systemReducer } from "./System";

const rootReducer = combineReducers({
  systemReducer,
});

export type RootState = ReturnType<typeof rootReducer>;
export { rootReducer };
