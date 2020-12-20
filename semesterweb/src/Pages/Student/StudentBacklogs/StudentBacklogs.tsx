import * as React from "react";
import { Redirect } from "react-router";
import { makeStyles, Theme } from "@material-ui/core";
import Fade from "@material-ui/core/Fade";
import { ScoreReciept } from "../../../Objects/ScoreReciept";
import { getStudentBacklogs } from "../../../Api/Student";
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

function StudentBacklogs({ studentId }: RouteParams): JSX.Element {
  // Hooks
  const classes = useStyles();

  const [data, setdata] = React.useState<Array<ScoreReciept>>(null);
  const [isDataFetched, setDataFetched] = React.useState(false);

  const fetchData = React.useCallback(async () => {
    setDataFetched(false);
    const response = await getStudentBacklogs(studentId);
    setdata(response);
    setDataFetched(true);
  }, [studentId]);

  React.useEffect(() => {
    fetchData();
  }, [fetchData, studentId]);

  if (isDataFetched && data !== null && data.length > 0) {
    return (
      <div className={classes.root}>
        <HeaderCard content={`Backlogs for Student:${studentId}`} />
        <Fade in timeout={2000}>
          <TableCardArray
            data={data}
            alignment={["left", "right", "right", "right"]}
          />
        </Fade>
        <ReturnToHomeCard content="Go Back" />
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

export default StudentBacklogs;
