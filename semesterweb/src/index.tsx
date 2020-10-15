import "./index.css";
import "fontsource-roboto";

import * as React from "react";
import * as ReactDOM from "react-dom";
import { Provider as StoreProvider } from "react-redux";
import { createStore } from "redux";
import { rootReducer } from "./Store";
import App from "./App";

const root = document.getElementById("root");

const Root = () => {
  const store = createStore(rootReducer);
  return (
    <StoreProvider store={store}>
      <App />
    </StoreProvider>
  );
};

ReactDOM.render(<Root />, root);
