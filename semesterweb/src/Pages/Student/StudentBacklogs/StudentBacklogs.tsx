import * as React from "react";
import { Redirect } from "react-router";
import Paper from "@material-ui/core/Paper";
import Table from "@material-ui/core/Table";
import TableRow from "@material-ui/core/TableRow";
import TableBody from "@material-ui/core/TableBody";
import TableCell from "@material-ui/core/TableCell";
import TableHead from "@material-ui/core/TableHead";
import TableContainer from "@material-ui/core/TableContainer";
import { makeStyles, Theme } from "@material-ui/core";
import Fade from "@material-ui/core/Fade";
import { IScoreReciept } from "../../../Objects/ScoreReciept";
import { getStudentBacklogs } from "../../../Api/Student";
import LoadingCard from "../../CommonComponents/LoadingCard";
import HeaderCard from "../../CommonComponents/HeaderCard";
import ReturnToHomeCard from "../../CommonComponents/ReturnToHomeCard";

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
  backlogCardRoot: {
    flex: 1,
    display: "flex",
    padding: theme.spacing(2),
    marginBottom: theme.spacing(3),
  },
  buttonCard: {
    flex: 1,
    display: "flex",
    justifyContent: "space-evenly",
  },
}));

function StudentBacklogs({ studentId }: RouteParams): JSX.Element {
  // Hooks
  const classes = useStyles();

  const [data, setdata] = React.useState<Array<IScoreReciept>>(null);
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
          <Paper className={classes.backlogCardRoot} elevation={10}>
            <TableContainer>
              <Table>
                <TableHead>
                  <TableRow>
                    <TableCell align="left">SubjectCode</TableCell>
                    <TableCell align="right">Internals</TableCell>
                    <TableCell align="right">Externals</TableCell>
                    <TableCell align="right">Total</TableCell>
                  </TableRow>
                </TableHead>
                <TableBody>
                  {data.map((val: IScoreReciept) => {
                    return (
                      <TableRow key={`StudentBacklog+${val.SubjectCode}`}>
                        <TableCell>{val.SubjectCode}</TableCell>
                        <TableCell align="right">{val.Internals}</TableCell>
                        <TableCell align="right">{val.Externals}</TableCell>
                        <TableCell align="right">
                          {val.Internals + val.Externals}
                        </TableCell>
                      </TableRow>
                    );
                  })}
                </TableBody>
              </Table>
            </TableContainer>
          </Paper>
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
