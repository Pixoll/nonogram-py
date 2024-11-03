from pygame import Surface

from components import NonogramElement, Element
from components.scroll_bar import ScrollBar
from core.nonogram import Nonogram
from events import Event


class NonogramElementWithScroll(Element):
    _nonogram_element: NonogramElement
    _scroll: ScrollBar

    def __init__(self,showContent:int, nonogram: Nonogram, block_size: int, padding: int):
        super().__init__(showContent, showContent)
        self._nonogram_element = NonogramElement(nonogram, block_size, padding)

        self._scroll = ScrollBar(200, self._nonogram_element.size[0])

    def set_position(self, position: tuple[int, int]) -> None:
        self._nonogram_element.set_position(position)
        scroll_position = (position[0], position[1] + self._nonogram_element.size[1] + self._scroll.size[1])
        self._scroll.set_position(scroll_position)

        pass

    def on_any_event(self, event: Event) -> None:
        self._nonogram_element.on_any_event(event)
        self._scroll.on_any_event(event)

    def update(self):
        self._scroll.update()
        scroll_offset = self._scroll.x_axis
        self._nonogram_element.set_position((self._nonogram_element.position[0]+scroll_offset,self._nonogram_element.position[1]))

    def get_nonogram_element(self) -> NonogramElement:
        return self._nonogram_element

    def render(self, window: Surface) -> None:
        self.update()
        self._nonogram_element.render(window)
        self._scroll.render(window)
        pass



