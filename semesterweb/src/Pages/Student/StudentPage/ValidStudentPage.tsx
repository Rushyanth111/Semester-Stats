import * as React from "react";

import Card from "@material-ui/core/Card";
import CardContent from "@material-ui/core/CardContent";
import CircularProgress from "@material-ui/core/CircularProgress";
import Grow from "@material-ui/core/Grow";
import StudentReciept from "../../../Objects/StudentReciept";

interface RouteParams {
  studentId: string;
}

async function sleep(ms: number): Promise<any> {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

async function dummyFetch(): Promise<StudentReciept> {
  const sampleData: StudentReciept = {
    Usn: "1CR17CS117",
    Name: "Rushyanth S",
    Batch: 2017,
    Department: "CS",
  };
  await sleep(3000);
  return sampleData;
}

export default function ValidStudent({ studentId }: RouteParams): JSX.Element {
  const [isDataFetched, setDataFetched] = React.useState(false);
  const [data, setData] = React.useState<StudentReciept>(null);

  const fetchData = React.useCallback(async () => {
    setDataFetched(false);
    const response = await dummyFetch();
    setData(response);
    setDataFetched(true);
  }, []);
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
            <CardContent>
              {data.Name}, {data.Usn}, {data.Batch}, {data.Department}
            </CardContent>
          </Card>
        </Grow>
      </div>
    );
  }

  // By Default, Load in the Loading Animation

  return <CircularProgress />;
}
