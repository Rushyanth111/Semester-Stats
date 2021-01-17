import * as React from "react";
import {
  Route,
  RouteComponentProps,
  Switch,
  useRouteMatch,
} from "react-router-dom";

import BatchSearch from "./BatchSearch";

interface SpecificBatch {
  batch: number;
}

function BatchRoutes(): JSX.Element {
  const batchUrl = useRouteMatch({
    path: "/Batch",
    strict: true,
    sensitive: true,
  });

  return (
    <Switch>
      <Route path={`${batchUrl.path}`} component={BatchSearch} exact />
    </Switch>
  );
}

export default BatchRoutes;
