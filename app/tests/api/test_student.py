from api.crud import major as major_crud
from api.crud import region as region_crud
from api.crud import student as student_crud
from fastapi.encoders import jsonable_encoder
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.core.config import settings
from app.tests.factories.major import MajorFactory
from app.tests.factories.region import RegionFactory
from app.tests.factories.student import StudentFactory


def test_create_student(
    client: TestClient, superuser_token_headers: dict, db: Session
) -> None:
    major_in = MajorFactory.create()
    major = major_crud.create(db, obj_in=major_in)
    region_in = RegionFactory.create()
    region = region_crud.create(db, obj_in=region_in)

    data = StudentFactory.create(major_id=major.id, region_id=region.id)
    r = client.post(
        f"{settings.API_V1_STR}/students/", headers=superuser_token_headers, json=jsonable_encoder(data),
    )

    assert 200 <= r.status_code < 300
    created_student = r.json()
    assert created_student['name'] == data.name


def test_get_student(
    client: TestClient, superuser_token_headers: dict, db: Session
) -> None:
    major_in = MajorFactory.create()
    major = major_crud.create(db, obj_in=major_in)
    region_in = RegionFactory.create()
    region = region_crud.create(db, obj_in=region_in)

    student_in = StudentFactory.create(major_id=major.id, region_id=region.id)
    student = student_crud.create(db, obj_in=student_in)
    student_id = student.id
    r = client.get(
        f"{settings.API_V1_STR}/students/{student_id}", headers=superuser_token_headers,
    )

    assert 200 <= r.status_code < 300
    api_student = r.json()
    existing_student = student_crud.get(db, id=student_id)
    assert existing_student
    assert existing_student.name == api_student["name"]


def test_update_student(
    client: TestClient, superuser_token_headers: dict, db: Session
) -> None:
    major_in = MajorFactory.create()
    major = major_crud.create(db, obj_in=major_in)
    region_in = RegionFactory.create()
    region = region_crud.create(db, obj_in=region_in)

    student_in = StudentFactory.create(major_id=major.id, region_id=region.id)

    created_student = student_crud.create(db, obj_in=student_in)
    created_student_id = created_student.id
    data = StudentFactory.create(
        status=2, major_id=major.id, region_id=region.id)
    r = client.put(
        f"{settings.API_V1_STR}/students/{created_student_id}", headers=superuser_token_headers, json=jsonable_encoder(data),
    )

    updated_student = r.json()
    assert 200 <= r.status_code < 300
    assert updated_student['id'] == created_student_id
    assert updated_student['name'] == data.name


def test_retrieve_students(
    client: TestClient, superuser_token_headers: dict, db: Session
) -> None:
    major_in = MajorFactory.create()
    major = major_crud.create(db, obj_in=major_in)
    region_in = RegionFactory.create()
    region = region_crud.create(db, obj_in=region_in)

    student_in = StudentFactory.create(major_id=major.id, region_id=region.id)
    student_crud.create(db, obj_in=student_in)

    student_in = StudentFactory.create(major_id=major.id, region_id=region.id)
    student_crud.create(db, obj_in=student_in)

    r = client.get(f"{settings.API_V1_STR}/students/",
                   headers=superuser_token_headers)

    all_users = r.json()

    assert len(all_users) > 1
    for item in all_users:
        assert "name" in item
