import * as React from "react";

interface RouteParams {
  studentId: string;
}

export default function StudentPage({ studentId }: RouteParams): JSX.Element {
  return <h1>Welcome to Specific Page of {studentId}</h1>;
}
