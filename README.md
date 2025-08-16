# badge-pinyin

A Pinyin input method for the [Shipwrecked PCB Badge](https://github.com/mpkendall/shipwrecked-pcb)

## Installation

1. Go to [https://badge.shipwrecked.hackclub.com/](https://badge.shipwrecked.hackclub.com/) and connect your badge.
2. Flash & update firmware if needed.
3. Upload the `pinyin_ime.zip` file in this repository.

**Warning:** The decompressed app size is around 1 MB. Please temporarily remove existing apps on your badge to avoid running out of space. The upload process may take 30 minutes or more.

## Interface

The input interface is a 8 row, 3 column grid of characters. A diagram of button functions is shown below:

| | Col 1 | Col 2 | Col 3 | |
|:-:|:-:|:-:|:-:|:-:|
| **Row 1** | | | | **Row 5** |
| **Row 2** | | | | **Row 6** |
| **Row 3** | | | | **Row 7** |
| **Row 4** | | | | **Row 8** |
| **Exit app** | **N/A** | **Clear** | **N/A** | **Page** |

- Select a character by pressing the corresponding **row and column buttons** together (Row & Col numbers start from the top left)
- **Page**: Flips through pages if there are more than 24 options (only when selecting Chinese characters, not typing the Pinyin)
- **Clear**: Clears the current Chinese character being composed, otherwise deletes the last character typed

## Usage

- Type the Pinyin (including the tone as a number) of a character. e.g. `ni3` for 你, `de ` (space for neutral tone) for 的
- Select the desired character from the options shown
- Repeat for more characters