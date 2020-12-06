import * as React from "react";

import {
  Route,
  RouteComponentProps,
  Switch,
  useRouteMatch,
} from "react-router-dom";

import Fade from "@material-ui/core/Fade";
import StudentPage from "./StudentPage";
import StudentSearch from "./SearchScreen";

interface SpecificStudent {
  studentId: string;
}

function StudentRoutes(): JSX.Element {
  const studentUrl = useRouteMatch();

  return (
    <Switch>
      <Route
        path={`${studentUrl.path}/:studentId`}
        render={({ match }: RouteComponentProps<SpecificStudent>) => (
          <Fade>
            <StudentPage studentId={match.params.studentId} />
          </Fade>
        )}
      />
      <Route path={studentUrl.path} exact>
        <StudentSearch />
      </Route>
    </Switch>
  );
}

export default StudentRoutes;
