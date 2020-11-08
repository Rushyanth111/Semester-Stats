import "./index.css";
import "fontsource-roboto";

import * as React from "react";
import * as ReactDOM from "react-dom";
import { Provider as StoreProvider } from "react-redux";
import { createStore } from "redux";
import { BrowserRouter } from "react-router-dom";
import { rootReducer } from "./Store";
import App from "./App";

const root = document.getElementById("root");

const Root = () => {
  const store = createStore(rootReducer);
  return (
    <BrowserRouter>
      <StoreProvider store={store}>
        <App />
      </StoreProvider>
    </BrowserRouter>
  );
};

ReactDOM.render(<Root />, root);
