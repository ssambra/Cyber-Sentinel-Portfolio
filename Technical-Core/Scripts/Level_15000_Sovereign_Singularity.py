# 5. Create the technical vault
mkdir -p Technical-Core

# 6. Move the core folders into the new unified vault
# (This preserves your work while cleaning up the root directory)
git mv Intelligence Technical-Core/ 2>/dev/null
git mv Scripts Technical-Core/ 2>/dev/null
git mv Shield Technical-Core/ 2>/dev/null
git mv Vault Technical-Core/ 2>/dev/null

# 7. Commit and push the final architecture
git add .
git commit -m "ARCHITECTURE UNIFIED: DORA-ENISA Master Repo Established"
git push origin main
