import * as React from "react";

import Card from "@material-ui/core/Card";
import CardContent from "@material-ui/core/CardContent";
import CircularProgress from "@material-ui/core/CircularProgress";
import Grow from "@material-ui/core/Grow";
import { IStudentReciept } from "../../../Objects/StudentReciept";
import { getStudent } from "../../../Api/Student";

interface RouteParams {
  studentId: string;
}

async function dummyFetch(usn: string): Promise<IStudentReciept> {
  const sampleData: IStudentReciept = await getStudent(usn);
  console.log(sampleData);
  return sampleData;
}

export default function ValidStudent({ studentId }: RouteParams): JSX.Element {
  const [isDataFetched, setDataFetched] = React.useState(false);
  const [data, setData] = React.useState<IStudentReciept>(null);

  const fetchData = React.useCallback(async () => {
    setDataFetched(false);
    const response = await dummyFetch(studentId);
    setData(response);
    setDataFetched(true);
  }, [studentId]);
  // Call Fetch to Execute
  React.useEffect(() => {
    fetchData();
  }, [fetchData]);

  // Check if There's Data and Render the Correct Card

  if (isDataFetched) {
    return (
      <div>
        <Grow in>
          <Card>
            <CardContent>{data.Name}</CardContent>
          </Card>
        </Grow>
      </div>
    );
  }

  // By Default, Load in the Loading Animation

  return <CircularProgress />;
}
