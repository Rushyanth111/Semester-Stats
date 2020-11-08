import * as React from "react";
import { Switch, Route } from "react-router-dom";
import Home from "./Pages/Home";
import Batch from "./Pages/Batch";
import Subject from "./Pages/Subject";
import Student from "./Pages/Student";
import Summary from "./Pages/Summary";

function Routes(): JSX.Element {
  return (
    <Switch>
      <Route path="/" exact>
        <Home />
      </Route>
      <Route path="/Batch">
        <Batch />
      </Route>
      <Route path="/Subject">
        <Subject />
      </Route>
      <Route path="/Student">
        <Student />
      </Route>
      <Route path="/Summary">
        <Summary />
      </Route>
    </Switch>
  );
}

export default Routes;
