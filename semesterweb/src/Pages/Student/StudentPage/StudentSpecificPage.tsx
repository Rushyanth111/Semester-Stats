import * as React from "react";

import InvalidStudent from "./InvalidStudent";
import ValidStudent from "./ValidStudentPage";

interface RouteParams {
  studentId: string;
}

function isUsnValid(usn: string): boolean {
  const pattern = new RegExp(/[A-Z0-9]{3}[0-9]{2}[A-Z]{2}[0-9]{3}/g);

  return pattern.test(usn);
}

export default function StudentSpecificPage({
  studentId,
}: RouteParams): JSX.Element {
  return (
    <>
      {isUsnValid(studentId) ? (
        <ValidStudent studentId={studentId} />
      ) : (
        <InvalidStudent />
      )}
    </>
  );
}
