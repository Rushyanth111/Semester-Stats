function isUsnValid(usn: string): boolean {
  const pattern = new RegExp(/[A-Z0-9]{3}[0-9]{2}[A-Z]{2}[0-9]{3}/g);
  return pattern.test(usn);
}

function isSubjectValid(subCode: string): boolean {
  const pattern = new RegExp(/[0-9]{2}[A-Z]{2,6}[0-9]{2,3}/);

  return pattern.test(subCode);
}

export { isUsnValid, isSubjectValid };
