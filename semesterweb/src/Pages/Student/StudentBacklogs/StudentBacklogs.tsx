import * as React from "react";

interface RouteParams {
  studentId: string;
}

function StudentBacklogs({ studentId }: RouteParams) {
  return <div>{studentId}</div>;
}

export default StudentBacklogs;
