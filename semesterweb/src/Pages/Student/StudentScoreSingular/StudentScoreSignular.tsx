import * as React from "react";

import { makeStyles, Theme } from "@material-ui/core";
import { Redirect } from "react-router";
import Fade from "@material-ui/core/Fade";
import TableCard from "../../CommonComponents/TableCard";
import { getStudentSubject } from "../../../Api/Student";
import LoadingCard from "../../CommonComponents/LoadingCard";
import { ScoreReciept } from "../../../Objects/ScoreReciept";
import HeaderCard from "../../CommonComponents/HeaderCard";
import ReturnToHomeCard from "../../CommonComponents/ReturnToHomeCard";

interface RouteParams {
  studentId: string;
  subjectCode: string;
}

const useStyles = makeStyles((theme: Theme) => ({
  root: {
    flex: 1,
    display: "flex",
    padding: theme.spacing(3),
    flexDirection: "column",
  },
}));

function StudentScoreSingular({
  studentId,
  subjectCode,
}: RouteParams): JSX.Element {
  const classes = useStyles();
  const [isDataFetched, setDataFetched] = React.useState(false);
  const [data, setData] = React.useState<ScoreReciept>(null);

  const fetchData = React.useCallback(async () => {
    setDataFetched(false);
    const response = await getStudentSubject(studentId, subjectCode);
    setData(response);
    setDataFetched(true);
  }, [studentId, subjectCode]);

  // Call Fetch to Execute
  React.useEffect(() => {
    fetchData();
  }, [studentId, fetchData]);

  // If Data is fetched.
  if (isDataFetched && data !== null) {
    return (
      <div className={classes.root}>
        <HeaderCard content="Score Details" />
        <Fade in timeout={1500}>
          <TableCard data={data} alignment={["left", "right"]} />
        </Fade>
        <ReturnToHomeCard content="Go Back to Search Page" />
      </div>
    );
  }

  if (isDataFetched && data === null) {
    return <Redirect to="/Student/NotFound" />;
  }

  return <LoadingCard />;
}

export default StudentScoreSingular;
