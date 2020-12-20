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
      <Route path="/Batch" component={Batch} />
      <Route path="/Subject" component={Subject} />
      <Route path="/Student" component={Student} />
      <Route path="/Summary" component={Summary} />
      <Route path="/" exact component={Home} />
    </Switch>
  );
}

export default Routes;
