import * as React from "react";
import ValidStudent from "./ValidStudentPage";
import { isUsnValid } from "../../../Helpers";

interface RouteParams {
  studentId: string;
}

function StudentSpecificPage({ studentId }: RouteParams): JSX.Element {
  if (isUsnValid(studentId)) {
    return <ValidStudent studentId={studentId} />;
  }

  return (
    <div>
      <h1>No, Thats not a Correct Usn</h1>
    </div>
  );
}

export default StudentSpecificPage;
