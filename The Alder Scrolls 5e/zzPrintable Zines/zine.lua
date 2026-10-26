-- Tables stay exactly where they appear in the source
function Table(el)
  local n = #el.colspecs
  local widths = {}
  for i = 1, n do widths[i] = 3 end

  -- Measure the longest content in each column (header + body)
  for _, row in ipairs(el.head.rows) do
    for i, cell in ipairs(row.cells) do
      local len = #pandoc.utils.stringify(cell.contents)
      if len > widths[i] then widths[i] = len end
    end
  end

  local row_count = #el.head.rows
  for _, body in ipairs(el.bodies) do
    for _, row in ipairs(body.body) do
      for i, cell in ipairs(row.cells) do
        local len = #pandoc.utils.stringify(cell.contents)
        if len > widths[i] then widths[i] = len end
      end
      row_count = row_count + 1
    end
  end

  -- Normalize to fractions that sum to 1
  local total = 0
  for i = 1, n do total = total + widths[i] end
  for i, spec in ipairs(el.colspecs) do
    el.colspecs[i] = {spec[1], widths[i] / total}
  end

  el.classes:insert("float")
  el.attributes["latex-placement"] = "!htbp"

  local needspace = pandoc.RawBlock('latex',
    string.format('\\needspace{%d\\baselineskip}', math.ceil(row_count * 1.8)))

  return { needspace, el }
end

-- <!-- pagebreak --> in source becomes \pagebreak in LaTeX
function RawBlock(el)
  if el.format == 'html' and el.text:find('pagebreak', 1, true) then
    return pandoc.RawBlock('latex', '\\pagebreak')
  end
  return el
end

-- Promote "X Spell List" headings to top level
-- (Two triggers: .toplevel class, or a heading ending in "Spell List")
function Header(el)
  if el.classes:includes('toplevel') then
    el.level = 1
    return el
  end
  if el.level == 2 and pandoc.utils.stringify(el.content):match('Spell List$') then
    el.level = 1
  end
  return el
end

-- Remove horizontal rules between spells
function HorizontalRule(el)
  return {}
end