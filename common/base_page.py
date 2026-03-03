# -*- coding:utf-8 -*-
from playwright.async_api import Page, Locator
from typing import Union
"""
    定义一个基类，封装常用的页面方法
"""
class BasePage:
    def __init__(self, page: Page):
        self.page = page
    
    async def wait_for_selector(self, selector: str,time: int) -> Locator:
        return await self.page.wait_for_selector(selector,timeout=time, state="visible")
    
    # 单击
    # 右击/左击/中间点击："right", "left", "middle"
    # shift+click: ["shift"]
    async def click(self, selector: str,action: str=None,modifiers: list=None):
        return await self.page.locator(selector).click(button=action,modifiers=modifiers)
    
    # 双击
    async def dbclick(self, selector: str):
        return await self.page.locator(selector).dblclick()
    
    #鼠标悬浮
    async def hover(self, selector: str):
        return await self.page.locator(selector).hover()
    
    # 填充文字
    async def fill(self, selector: str, text: str):
        return await self.page.fill(selector, text)
    
    # select下拉选择 单选/多选
    async def select_option(self, selector: str, value: Union[str, list]):
        return await self.page.select_option(selector, value)
    
    async def get_by_role(self, role: str, name: str = None):
        return await self.page.get_by_role(role, name=name)
    
    async def get_by_placeholder(self, text: Union[str, list]):
        return await self.page.get_by_placeholder(text)
    
    async def get_by_label(self, text: Union[str, list]):
        return await self.page.get_by_label(text)
    

        

    