import * as React from "react";
import { Redirect } from "react-router";
import { makeStyles, Theme } from "@material-ui/core";
import Fade from "@material-ui/core/Fade";
import { ScoreReciept } from "../../../Objects/ScoreReciept";
import { getStudentScores } from "../../../Api/Student";
import LoadingCard from "../../CommonComponents/LoadingCard";
import HeaderCard from "../../CommonComponents/HeaderCard";
import ReturnToHomeCard from "../../CommonComponents/ReturnToHomeCard";
import TableCardArray from "../../CommonComponents/TableCardArray";

interface RouteParams {
  studentId: string;
}

const useStyles = makeStyles((theme: Theme) => ({
  root: {
    flex: 1,
    display: "flex",
    flexDirection: "column",
    margin: theme.spacing(2),
  },
}));

function StudentScores({ studentId }: RouteParams): JSX.Element {
  // Hooks
  const classes = useStyles();
  const [data, setData] = React.useState<Array<ScoreReciept>>(null);
  const [isDataFetched, setDataFetched] = React.useState(false);

  const fetchData = React.useCallback(async () => {
    setDataFetched(false);
    const response = await getStudentScores(studentId);
    console.log(response);
    setData(response);
    setDataFetched(true);
  }, [studentId]);

  React.useEffect(() => {
    fetchData();
  }, [studentId, fetchData]);

  if (isDataFetched && data !== null && data.length > 0) {
    return (
      <div className={classes.root}>
        <HeaderCard content={`Scores for Usn:${studentId}`} />
        <Fade in timeout={2500}>
          <TableCardArray
            data={data}
            alignment={["left", "right", "right", "right"]}
          />
        </Fade>
        <ReturnToHomeCard content="Go Back to Search Screen" />
      </div>
    );
  }
  if (
    (isDataFetched && data !== null && data.length === 0) ||
    (isDataFetched && data === null)
  ) {
    return <Redirect to="/Student/NotFound" />;
  }

  return <LoadingCard />;
}

export default StudentScores;
