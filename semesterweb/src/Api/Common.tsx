// I'm not sure what having multiple copies of the same statement is going to accomplish,
// so here is code to mitigate that.
import axios, { AxiosResponse } from "axios";
import Report from "../Objects/Report";
import { urlWrapper, URLParams } from "./URLWrapper";

async function get<T>(
  url: string,
  params?: URLParams
): Promise<AxiosResponse<T>> {
  /**
   * @description Function to return the result of an API call.
   * @param url Full/Relative URL of the API
   */
  const newUrl = urlWrapper(url, params);
  const response = await axios.get<T>(newUrl);
  return response;
}

async function post<T extends Report<T>>(url: string, Obj: T): Promise<void> {
  const response = await axios.post(url, Obj.toObj());
  if (response.status !== 201) {
    throw new Error(
      `Returned StatusCode: ${response.status}||${response.statusText}`
    );
  }
}

const put = post;

export { get, post, put };
