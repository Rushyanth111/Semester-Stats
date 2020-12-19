import * as React from "react";
import { isSubjectValid, isUsnValid } from "../../../Helpers";

interface RouteParams {
  studentId: string;
  subjectCode: string;
}

function StudentScoreSpecificPage({
  studentId,
  subjectCode,
}: RouteParams): JSX.Element {
  if (isSubjectValid(subjectCode) && isUsnValid(studentId)) {
    return (
      <div>
        {studentId} {subjectCode}
      </div>
    );
  }

  return (
    <div>
      <h1>No, That`s not a Correct SubjectCode</h1>
    </div>
  );
}

export default StudentScoreSpecificPage;
