import { makeStyles } from "@material-ui/core";
import * as React from "react";
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
    <div className={classes.StudentSearchScreenRoot}>
      <StudentSearch />
      <StudentScoreSearch />
    </div>
  );
}

export default StudentGoTo;
