ActiveRecord::Schema.define(version: 20150321234554) do

  # These are extensions that must be enabled in order to support this database
  enable_extension "plpgsql"

  create_table "games", force: :cascade do |t|
    t.datetime "created_at"
    t.datetime "updated_at"
    t.integer  "team_1_score",      default: 0
    t.integer  "team_2_score",      default: 0
    t.boolean  "in_progress",       default: false
    t.integer  "team_1_defense_id",                 null: false
    t.integer  "team_1_offense_id",                 null: false
    t.integer  "team_2_offense_id",                 null: false
    t.integer  "team_2_defense_id",                 null: false
  end

  create_table "players", force: :cascade do |t|
    t.datetime "created_at"
    t.datetime "updated_at"
    t.string   "nickname",   null: false
  end

end
