from sqlalchemy.orm import Session

from semesterstat.database.models import BatchSchemeInfo, Department


def __input_data(db: Session):
    depts = [
        {"Code": code, "Name": name}
        for (code, name) in [
            ("CS", "Computer Science"),
            ("IS", "Information Science"),
            ("TE", "Telecommunication"),
            ("ME", "Mechanical Engineering"),
            ("AE", "Aeronautical Engineering"),
        ]
    ]

    db.bulk_insert_mappings(Department, depts)

    batch_scheme = [
        {"Batch": batch, "Scheme": scheme}
        for (batch, scheme) in [(2015, 2015), (2016, 2015), (2017, 2017)]
    ]
    db.bulk_insert_mappings(BatchSchemeInfo, batch_scheme)
