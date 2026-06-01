
todo_list = []


def add_todo(task):

    new_item = {"task": task, "done": False}
    todo_list.append(new_item)
    print(f"'{task}'이(가) 추가되었습니다.")

def show_todos():
    if not todo_list:
        print("할 일이 없습니다.")
        return
 
    print("\n" + "=" * 30)
    print("       할 일 목록")
    print("=" * 30)
 
    for i, item in enumerate(todo_list, 1):

        if item["done"] == True:
            status = "✓"
        else:
            status = " "
        print(f"  {i}. [{status}] {item['task']}")
 
    print("=" * 30)


def complete_todo(index):

    if index < 1 or index > len(todo_list):
        print("올바르지 않은 번호입니다.")
        return
    todo_list[index - 1]["done"] = True
    task = todo_list[index - 1]["task"]
    print(f"'{task}'을 완료했습니다.")


def count_todos():
    """전체 항목 수와 완료된 항목 수를 반환한다.

    Returns:
        tuple: (전체 수, 완료 수)

    Example:
        total, done = count_todos()
        print(f"전체 {total}개 중 {done}개 완료")
    """
    total = len(todo_list)
    # TODO: 완료된 항목 수를 계산하세요
    #       힌트: item["done"]이 True인 항목의 수를 세어보세요
    done = 0
    return total, done


if __name__ == "__main__":
    # 아래 테스트 코드를 실행하여 각 함수가 올바르게 동작하는지 확인하세요
    # 이 블록은 수정하지 마세요

    add_todo("파이썬 과제 완료하기")
    add_todo("Git 실습 지시서 읽기")
    add_todo("README.md 작성하기")
    show_todos()

    complete_todo(1)
    show_todos()

    total, done = count_todos()
    print(f"\n전체 {total}개 중 {done}개 완료")