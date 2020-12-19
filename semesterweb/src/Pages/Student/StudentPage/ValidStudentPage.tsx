import * as React from "react";

import Card from "@material-ui/core/Card";
import CardContent from "@material-ui/core/CardContent";
import CircularProgress from "@material-ui/core/CircularProgress";
import Grow from "@material-ui/core/Grow";
import { Dispatch } from "redux";
import { connect, ConnectedProps } from "react-redux";
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

function ValidStudent({
  studentId,
  setLoading,
}: RouteParams & PropsFromRedux): JSX.Element {
  const [isDataFetched, setDataFetched] = React.useState(false);
  const [data, setData] = React.useState<IStudentReciept>(null);

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

  // If Data is fetched.
  if (isDataFetched) {
    return (
      <div>
        <Grow in timeout={1000}>
          <Card>
            <CardContent>
              {data === null ? "This Student Does not Exist" : data.Name}
            </CardContent>
          </Card>
        </Grow>
      </div>
    );
  }

  return <CircularProgress />;
}

export default connector(ValidStudent);
