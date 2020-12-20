import { makeStyles } from "@material-ui/core";
import * as React from "react";
import Fade from "@material-ui/core/Fade";
import { StudentSearch, StudentScoreSearch } from "./Feilds";

const useStyles = makeStyles(() => ({
  StudentSearchScreenRoot: {
    flex: 1,
    display: "flex",
    flexDirection: "column",
  },
}));

function StudentGoTo(): JSX.Element {
  const classes = useStyles();
  return (
    <Fade in timeout={1500}>
      <div className={classes.StudentSearchScreenRoot}>
        <StudentSearch />
        <StudentScoreSearch />
      </div>
    </Fade>
  );
}

export default StudentGoTo;
