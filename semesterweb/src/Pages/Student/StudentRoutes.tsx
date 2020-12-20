import * as React from "react";

import {
  Route,
  RouteComponentProps,
  Switch,
  useRouteMatch,
} from "react-router-dom";

import StudentPage from "./StudentPage";
import StudentSearch from "./SearchScreen";
import StudentScores from "./StudentScores";
import StudentBacklog from "./StudentBacklogs";
import StudentScoreSingular from "./StudentScoreSingular";

interface SpecificStudent {
  studentId: string;
}

interface SpecificSubject {
  subjectCode: string;
}

function StudentRoutes(): JSX.Element {
  const studentUrl = useRouteMatch({
    path: "/Student",
    strict: true,
    sensitive: true,
  });

  return (
    <Switch>
      <Route
        path={`${studentUrl.path}/Backlogs/:studentId`}
        render={({ match }: RouteComponentProps<SpecificStudent>) => (
          <StudentBacklog studentId={match.params.studentId} />
        )}
      />
      <Route
        path={`${studentUrl.path}/Scores/:studentId`}
        render={({
          match,
        }: RouteComponentProps<SpecificStudent & SpecificSubject>) => (
          <StudentScores studentId={match.params.studentId} />
        )}
      />
      <Route
        path={`${studentUrl.path}/Score/:studentId/:subjectCode`}
        render={({
          match,
        }: RouteComponentProps<SpecificStudent & SpecificSubject>) => (
          <StudentScoreSingular
            studentId={match.params.studentId}
            subjectCode={match.params.subjectCode}
          />
        )}
      />
      <Route
        path={`${studentUrl.path}/:studentId`}
        render={({ match }: RouteComponentProps<SpecificStudent>) => (
          <StudentPage studentId={match.params.studentId} />
        )}
      />
      <Route path={studentUrl.path} component={StudentSearch} />
    </Switch>
  );
}

export default StudentRoutes;
