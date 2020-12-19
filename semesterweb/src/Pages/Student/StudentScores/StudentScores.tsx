import * as React from "react";

interface RouteParams {
  studentId: string;
}

function StudentScores({ studentId }: RouteParams): JSX.Element {
  return <div>{studentId}</div>;
}

export default StudentScores;
