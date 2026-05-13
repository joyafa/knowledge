"""验证预加载模块在模拟 Streamlit rerun 场景下的正确性。"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))

from rag.preload import state, start, is_done, get_chain, reset


def test_preload_survives_rerun_simulation():
    """模拟 Streamlit 多次 rerun：模块不会重置状态。"""
    # 初始状态
    assert not is_done()
    assert get_chain() is None

    # 第一次"运行"：启动预加载
    start()
    assert state["started"] is True

    # 模拟 Streamlit rerun：重新 import rag.preload
    # Python 不会重新执行模块顶层代码，所以状态保持不变
    import rag.preload as p2
    assert p2.is_done() == state["done"]  # 同一个对象
    assert p2.state is state  # 引用相同

    # 重置
    reset()
    assert not is_done()
    assert state["started"] is False

    print("✅ 预加载模块验证通过：状态在模拟 rerun 后保持不变")


if __name__ == "__main__":
    test_preload_survives_rerun_simulation()
