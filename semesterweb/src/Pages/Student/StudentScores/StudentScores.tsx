import * as React from "react";
import { Redirect, useHistory } from "react-router";
import Paper from "@material-ui/core/Paper";
import Table from "@material-ui/core/Table";
import TableRow from "@material-ui/core/TableRow";
import TableBody from "@material-ui/core/TableBody";
import TableCell from "@material-ui/core/TableCell";
import TableHead from "@material-ui/core/TableHead";
import TableContainer from "@material-ui/core/TableContainer";
import { makeStyles, Theme, Typography } from "@material-ui/core";
import Fade from "@material-ui/core/Fade";
import Card from "@material-ui/core/Card";
import CardContent from "@material-ui/core/CardContent";
import Button from "@material-ui/core/Button";
import { IScoreReciept } from "../../../Objects/ScoreReciept";
import { getStudentScores } from "../../../Api/Student";
import LoadingCard from "../../CommonComponents/LoadingCard";

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
  titleCard: {
    display: "flex",
    justifyContent: "center",
    marginBottom: theme.spacing(3),
    padding: theme.spacing(2),
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

function StudentScores({ studentId }: RouteParams): JSX.Element {
  // Hooks
  const history = useHistory();
  const classes = useStyles();
  const [data, setData] = React.useState<Array<IScoreReciept>>(null);
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

  const handleOnClickBack = () => {
    history.goBack();
  };

  if (isDataFetched && data !== null && data.length > 0) {
    return (
      <div className={classes.root}>
        <Fade in timeout={1500}>
          <Paper className={classes.titleCard} elevation={5}>
            <Typography variant="h3">Backlogs for Usn: {studentId}</Typography>
          </Paper>
        </Fade>
        <Fade in timeout={2500}>
          <Paper className={classes.backlogCardRoot} elevation={10}>
            <TableContainer>
              <Table>
                <TableHead>
                  <TableRow>
                    <TableCell>Subject Code</TableCell>
                    <TableCell align="right">Internals</TableCell>
                    <TableCell align="right">Externals</TableCell>
                    <TableCell align="right">Total</TableCell>
                  </TableRow>
                </TableHead>
                <TableBody>
                  {data.map((val: IScoreReciept) => {
                    return (
                      <TableRow key={`StudentScores${val.SubjectCode}`}>
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
        <Fade in timeout={1500}>
          <Card className={classes.buttonCard} elevation={5}>
            <CardContent>
              <Button
                variant="outlined"
                color="secondary"
                onClick={handleOnClickBack}
              >
                Go Back to Search Screen.
              </Button>
            </CardContent>
          </Card>
        </Fade>
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
