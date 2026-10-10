import math
from motorbridge import MotorState


def make_state(pos: float, vel: float) -> MotorState:
    return MotorState(
        can_id=0,
        arbitration_id=0,
        status_code=0,
        pos=pos,
        vel=vel,
        torq=0.0,
        t_mos=0.0,
        t_rotor=0.0,
    )


def describe_state(state: MotorState | None) -> str:
    if state is None:
        return "尚未收到反馈"

    return (
        f"位置 {state.pos:.3f} rad，"
        f"角度 {math.degrees(state.pos):.3f} deg，"
        f"速度 {state.vel:.3f} rad/s"
    )


def main() -> None:
    print("合成数据，未连接电机")
    print(describe_state(None))
    print(describe_state(make_state(0.0, 0.0)))
    print(describe_state(make_state(math.pi / 2, -0.5)))


if __name__ == "__main__":
    main()
