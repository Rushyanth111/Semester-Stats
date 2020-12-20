import * as React from "react";

import Paper from "@material-ui/core/Paper";
import Table from "@material-ui/core/Table";
import TableRow from "@material-ui/core/TableRow";
import TableBody from "@material-ui/core/TableBody";
import TableCell from "@material-ui/core/TableCell";
import TableHead from "@material-ui/core/TableHead";
import TableContainer from "@material-ui/core/TableContainer";
import { makeStyles, Theme } from "@material-ui/core";
import Receipt from "../../../Objects";

interface Params<T> {
  data: T;
  alignment: ("left" | "right" | "inherit" | "center" | "justify")[];
  style?: React.CSSProperties;
}

const useStyles = makeStyles((theme: Theme) => ({
  tableRoot: {
    flex: 1,
    display: "flex",
    padding: theme.spacing(2),
    marginBottom: theme.spacing(3),
  },
}));

function TableCard<R extends Receipt>({
  data,
  alignment,
  style,
}: Params<R>): JSX.Element {
  const classes = useStyles();

  const HeaderData = Object.keys(data).map((val: string) => {
    return (
      <TableRow key={val}>
        <TableCell align={alignment[0]}>{val}</TableCell>
        <TableCell align={alignment[1]}>{data[val]}</TableCell>
      </TableRow>
    );
  });

  return (
    <div style={style}>
      <Paper className={classes.tableRoot} elevation={10}>
        <TableContainer>
          <Table>
            <TableHead>
              <TableRow>
                <TableCell align={alignment[0]}>Detail</TableCell>
                <TableCell align={alignment[1]}>Value</TableCell>
              </TableRow>
            </TableHead>
            <TableBody>{HeaderData}</TableBody>
          </Table>
        </TableContainer>
      </Paper>
    </div>
  );
}

export default TableCard;
