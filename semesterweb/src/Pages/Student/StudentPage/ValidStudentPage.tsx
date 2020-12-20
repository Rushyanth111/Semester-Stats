import * as React from "react";

import Card from "@material-ui/core/Card";
import CardContent from "@material-ui/core/CardContent";
import Grow from "@material-ui/core/Grow";
import { Dispatch } from "redux";
import { connect, ConnectedProps } from "react-redux";
import Table from "@material-ui/core/Table";
import TableBody from "@material-ui/core/TableBody";
import TableRow from "@material-ui/core/TableRow";
import TableCell from "@material-ui/core/TableCell";
import { makeStyles, Theme } from "@material-ui/core";
import Button from "@material-ui/core/Button";
import Fade from "@material-ui/core/Fade";
import Paper from "@material-ui/core/Paper";
import Typography from "@material-ui/core/Typography";
import { Redirect, useHistory } from "react-router";
import { IStudentReciept } from "../../../Objects/StudentReciept";
import { getStudent } from "../../../Api/Student";
import { toggleLoading } from "../../../Store/System";

interface RouteParams {
  studentId: string;
}

function mapStateToDispatch(dispatch: Dispatch) {
  return {
    setLoading: () => {
      dispatch(toggleLoading());
    },
  };
}

const connector = connect(null, mapStateToDispatch);
type PropsFromRedux = ConnectedProps<typeof connector>;

const useStyles = makeStyles((theme: Theme) => ({
  root: {
    flex: 1,
    display: "flex",
    padding: theme.spacing(3),
    flexDirection: "column",
  },
  title: {
    padding: theme.spacing(1),
    marginBottom: theme.spacing(2),
    display: "flex",
    justifyContent: "center",
  },
  detailCard: {
    flex: 1,
    marginBottom: theme.spacing(3),
  },
  buttonDivision: {
    display: "flex",
    flex: 1,
    justifyContent: "space-evenly",
  },
}));

function ValidStudent({
  studentId,
  setLoading,
}: RouteParams & PropsFromRedux): JSX.Element {
  const classes = useStyles();
  const [isDataFetched, setDataFetched] = React.useState(false);
  const [data, setData] = React.useState<IStudentReciept>(null);
  const history = useHistory();

  const fetchData = React.useCallback(async () => {
    setLoading();
    setDataFetched(false);
    const response = await getStudent(studentId);
    setData(response);
    setDataFetched(true);
    setLoading();
  }, [studentId, setLoading]);

  // Call Fetch to Execute
  React.useEffect(() => {
    fetchData();
  }, [studentId, fetchData]);

  const handleOnClickScores = () => {
    history.push(`/Student/Scores/${studentId}`);
  };

  const handleOnClickBacklogs = () => {
    history.push(`/Student/Scores/${studentId}`);
  };

  const handleOnClickBack = () => {
    history.push(`/Student`);
  };

  // If Data is fetched.
  if (isDataFetched && data !== null) {
    return (
      <div className={classes.root}>
        <Paper className={classes.title} elevation={5}>
          <Typography variant="h3">Student Details</Typography>
        </Paper>
        <Grow in timeout={1500}>
          <Card className={classes.detailCard} elevation={10}>
            <CardContent>
              <Table>
                <TableBody>
                  {Object.keys(data).map((key) => {
                    return (
                      <TableRow key={key} hover>
                        <TableCell align="left">{key}</TableCell>
                        <TableCell align="right">{data[key]}</TableCell>
                      </TableRow>
                    );
                  })}
                </TableBody>
              </Table>
            </CardContent>
          </Card>
        </Grow>
        <Fade in timeout={2500}>
          <Card elevation={5}>
            <CardContent>
              <div className={classes.buttonDivision}>
                <Button
                  color="secondary"
                  variant="outlined"
                  onClick={handleOnClickScores}
                >
                  View Student Scores
                </Button>
                <Button
                  color="secondary"
                  variant="outlined"
                  onClick={handleOnClickBacklogs}
                >
                  View Student Backlogs
                </Button>
                <Button
                  color="secondary"
                  variant="outlined"
                  onClick={handleOnClickBack}
                >
                  Go Back
                </Button>
              </div>
            </CardContent>
          </Card>
        </Fade>
      </div>
    );
  }

  if (isDataFetched && data === null) {
    return <Redirect to="/Student/NotFound" />;
  }

  return (
    <div className={classes.root}>
      <Paper>
        <Typography>Loading...</Typography>
      </Paper>
    </div>
  );
}

export default connector(ValidStudent);
