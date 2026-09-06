from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `course` ADD `addr` VARCHAR(32) NOT NULL COMMENT '教室' DEFAULT '';"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `course` DROP COLUMN `addr`;"""


MODELS_STATE = (
    "eJztmVuPmzgUx78K8lMrZVeEhNzeMtmOetnOSDPRaqVNhQwYgobY1JidptN895WNiYGELE"
    "zalEnzMpdzjo39sznnb/MEVsRFYfz7LIRfv4KJ9gQwXCEw0YqOjgZgFCkzNzBohyLS2YbY"
    "MaPQYWCieTCMUUcDLoodGkQsIBhMNJyEITcSJ2Y0wL4yJTj4nCCLER+xJaJgov3zqaOBAL"
    "voC4qzf6MHywtQ6BYGGrj82cJusXUkbO8wuxaB/Gm25ZAwWWEVHK3ZkuBtdIAZt/oIIwoZ"
    "4t0zmvDh89HJaWYzSkeqQtIh5tq4yINJyHLTtS1lA5Z1czu37t/MLQs0AOQQzOEGmHEaT8"
    "DnQ/jN6PaH/VFv0B91NCCGubUMN+mjFZi0ocBzMwcb4YcMphGCsYIqfu9gnS0h3c81iy+R"
    "jRktk804HkKbGRRbtZ+eDxcskmEPuYtkiOBwkZh9nf899nRQD/kKfrFChH225JxN8wDgv6"
    "Z3s7fTu1eGab7mvRMKnfRluZEuI/VtNnxfe3Jfbze6DZ2HR0hdq+BRyxOzxEV8XDtLdCVb"
    "Xn+4QyEUM99dFvlu36e9tGeFam9/iV5Z5esnaBKDVOHcda2MVdkCMfTFlPiz+ZOyVEgSGq"
    "O9STL1HM6SKuaSJi9pstVpcmR7aJEMoW6nafKnJshObhND16VNeGfxp+MNQGPaA9McLxLT"
    "hv3ncO4ZNTD3jErK3FWEzBB0lohajTJGsdH/Z47W7O+RbRuLxET6CJwspezU/B34u+SvCU"
    "WBjz+gtViAdzhmEDv7soksSnPV01mAr6r5HQ1Q+LiteKWdSLDlohCxNFFM72fTP96ATbXG"
    "OlJA1JFoHyFezwn/WXMlj9BpP6L6Ap6sBoNFMjS73iIZ6/o4W9nRaHD8aopZWyWJlWNAub"
    "BF7jYiVVYpaELFMj2gdW4N5FbYLqL0pu2kky0pSfxlvpVSbHs3UUcDVlkLbQ4KyGwOexRk"
    "bnrVElIO7KIhz0pDxpg0oCqjW15g0/xg9rzh6YpqXsJEj24TmSjDW67KTdvhSXekd1ujx8"
    "/0/GOO3V7LTj5OCONmijzXos3Z4qR5+IDw5ri+g+re3pe/MLp11XVuV/00aZ0XfMcpa3Vx"
    "98sKa4WgrKsLJ5iisC5I57KuLqru44W1YH9YWWdn3T3KOncMrlbWuVP3RVm/qIz+C97Otl"
    "CdsEZnGBndZlXC76pc43KGOdMzzLM+ulbKjibfXJ+vOF7UpewP/RA7RTRwlvuKvfQcrPVQ"
    "xVxK/bmU+n8RjeV7Vzdh5pq0OWnWR3yCz69R1Ojraxp+hnS7ul6DblfXK+kKX+mKh2Amr/"
    "eLhN/f395U3PGoJiXKbuAw7ZsWBjF7ubcR3h64HAbveRXHn8M801cfp3+Xcc/+vL0ScEjM"
    "fCp6ER1cNdMA37+Ybf4D2Cs8Lg=="
)
