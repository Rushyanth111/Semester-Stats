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

const useStyles = makeStyles((theme: Theme) => ({
  tableRoot: {
    flex: 1,
    display: "flex",
    padding: theme.spacing(2),
    marginBottom: theme.spacing(3),
  },
}));

interface Params<T> {
  data: Array<T>;
  alignment: ("left" | "right" | "inherit" | "center" | "justify")[];
  style?: React.CSSProperties;
}

function TableCardArray<R extends Receipt>({
  data,
  alignment,
  style,
}: Params<R>): JSX.Element {
  const classes = useStyles();

  const HeaderData = Object.keys(data[0]).map((val: string, idx: number) => {
    return <TableCell align={alignment[idx]}>{val}</TableCell>;
  });

  const BodyData = data.map((obj: R) => {
    return (
      <TableRow key={Object.keys(obj).join("")}>
        {Object.keys(obj).map((val: string, idx: number) => {
          return <TableCell align={alignment[idx]}>{obj[val]}</TableCell>;
        })}
      </TableRow>
    );
  });

  return (
    <div style={style}>
      <Paper className={classes.tableRoot} elevation={10}>
        <TableContainer>
          <Table>
            <TableHead>
              <TableRow>{HeaderData}</TableRow>
            </TableHead>
            <TableBody>{BodyData}</TableBody>
          </Table>
        </TableContainer>
      </Paper>
    </div>
  );
}

export default TableCardArray;
