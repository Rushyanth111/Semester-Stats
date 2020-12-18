interface URLParams {
  [key: string]: string | number;
}

function urlWrapper(url: string, params?: URLParams): string {
  // Url is already Defined, add in the URLParams.

  let modUrl = url;
  modUrl += "?";
  if (params) {
    Object.entries(params).forEach(([key, val]) => {
      // 0 is still valid, Empty things, however, are not.
      if (val || (typeof val === "number" && val === 0)) {
        modUrl += `${key}=${val}&`;
      }
    });
  }

  return modUrl.substring(0, modUrl.length - 1);
}

export { urlWrapper, URLParams };
