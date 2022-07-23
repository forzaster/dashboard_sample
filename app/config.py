from dataclasses import dataclass


@dataclass
class Config:
    is_local_test = True
    title = 'Test'
    sidebar_title = 'Sidebar'
    sidebar_width = 12
