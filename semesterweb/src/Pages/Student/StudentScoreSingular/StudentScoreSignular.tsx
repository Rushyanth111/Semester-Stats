import * as React from "react";

import Card from "@material-ui/core/Card";
import CardContent from "@material-ui/core/CardContent";
import Grow from "@material-ui/core/Grow";
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
import { getStudentSubject } from "../../../Api/Student";
import LoadingCard from "../../CommonComponents/LoadingCard";
import { IScoreReciept } from "../../../Objects/ScoreReciept";

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

function StudentScoreSingular({
  studentId,
  subjectCode,
}: RouteParams): JSX.Element {
  const classes = useStyles();
  const [isDataFetched, setDataFetched] = React.useState(false);
  const [data, setData] = React.useState<IScoreReciept>(null);
  const history = useHistory();

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

  const handleOnClickBack = () => {
    history.push(`/Student`);
  };

  // If Data is fetched.
  if (isDataFetched && data !== null) {
    return (
      <div className={classes.root}>
        <Paper className={classes.title} elevation={5}>
          <Typography variant="h3">Score Details</Typography>
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

  return <LoadingCard />;
}

export default StudentScoreSingular;
